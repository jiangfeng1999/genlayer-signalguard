import { createClient } from "https://esm.sh/genlayer-js@1.1.8?bundle";
import { studionet } from "https://esm.sh/genlayer-js@1.1.8/chains?bundle";
import { TransactionStatus } from "https://esm.sh/genlayer-js@1.1.8/types?bundle";

const CONTRACT_ADDRESS = "0x1d496901d68FC02d105A14B81Ea0e67476A9891A";

const connectButton = document.querySelector("#connectWallet");
const loadButton = document.querySelector("#loadVerdict");
const submitButton = document.querySelector("#submitReview");
const walletStatus = document.querySelector("#walletStatus");
const operationStatus = document.querySelector("#operationStatus");
const latestClaim = document.querySelector("#latestClaim");
const latestVerdict = document.querySelector("#latestVerdict");
const transactionLink = document.querySelector("#transactionLink");
const claimInput = document.querySelector("#claim");
const sourceInput = document.querySelector("#sourceUrl");

let writeClient = null;
let account = null;

function shortAddress(address) {
  return `${address.slice(0, 8)}...${address.slice(-6)}`;
}

function setStatus(message, kind = "neutral") {
  operationStatus.textContent = message;
  operationStatus.dataset.kind = kind;
}

function setBusy(isBusy) {
  connectButton.disabled = isBusy;
  loadButton.disabled = isBusy || !writeClient;
  submitButton.disabled = isBusy;
}

function validateReviewInput() {
  const claim = claimInput.value.trim();
  const sourceUrl = sourceInput.value.trim();
  if (claim.length < 8 || claim.length > 1000) {
    throw new Error("Claim must contain 8 to 1,000 characters.");
  }
  if (sourceUrl.length > 512) {
    throw new Error("Source URL must be 512 characters or fewer.");
  }
  const parsed = new URL(sourceUrl);
  if (parsed.protocol !== "https:") {
    throw new Error("Source URL must use HTTPS.");
  }
  return { claim, sourceUrl };
}

async function connectWallet() {
  if (!window.ethereum) {
    throw new Error("No injected wallet was detected. Open this page in a browser with MetaMask.");
  }
  const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
  if (!accounts.length) {
    throw new Error("The wallet did not return an account.");
  }
  account = accounts[0];
  writeClient = createClient({
    chain: studionet,
    account,
    provider: window.ethereum,
  });
  await writeClient.connect("studionet");
  walletStatus.textContent = `Connected ${shortAddress(account)}`;
  walletStatus.dataset.connected = "true";
  await loadCurrentVerdict();
}

async function loadCurrentVerdict() {
  if (!writeClient) {
    throw new Error("Connect a wallet to read live StudioNet state.");
  }
  const [claim, verdict] = await Promise.all([
    writeClient.readContract({
      address: CONTRACT_ADDRESS,
      functionName: "latest_claim",
      args: [],
      stateStatus: "accepted",
    }),
    writeClient.readContract({
      address: CONTRACT_ADDRESS,
      functionName: "latest_verdict",
      args: [],
      stateStatus: "accepted",
    }),
  ]);
  latestClaim.textContent = claim || "No accepted claim has been stored yet.";
  latestVerdict.textContent = verdict || "No accepted verdict has been stored yet.";
}

async function submitReview() {
  if (!writeClient || !account) {
    await connectWallet();
  }
  const { claim, sourceUrl } = validateReviewInput();
  const hash = await writeClient.writeContract({
    address: CONTRACT_ADDRESS,
    functionName: "review_claim",
    args: [claim, sourceUrl],
    value: 0n,
  });
  transactionLink.href = `https://genlayer-explorer.vercel.app/transactions/${hash}`;
  transactionLink.textContent = hash;
  transactionLink.hidden = false;
  setStatus("Transaction submitted. Waiting for an accepted receipt...", "working");
  await writeClient.waitForTransactionReceipt({
    hash,
    status: TransactionStatus.ACCEPTED,
  });
  await loadCurrentVerdict();
  setStatus("Review accepted and current contract state refreshed.", "success");
}

connectButton.addEventListener("click", async () => {
  setBusy(true);
  setStatus("Connecting wallet...", "working");
  try {
    await connectWallet();
    setStatus("Wallet connected to StudioNet.", "success");
  } catch (error) {
    setStatus(error.message, "error");
  } finally {
    setBusy(false);
  }
});

loadButton.addEventListener("click", async () => {
  setBusy(true);
  setStatus("Reading accepted contract state...", "working");
  try {
    await loadCurrentVerdict();
    setStatus("Accepted contract state loaded from StudioNet.", "success");
  } catch (error) {
    setStatus(error.message, "error");
  } finally {
    setBusy(false);
  }
});

submitButton.addEventListener("click", async () => {
  setBusy(true);
  setStatus("Preparing review transaction...", "working");
  try {
    await submitReview();
  } catch (error) {
    setStatus(error.message, "error");
  } finally {
    setBusy(false);
  }
});

setBusy(false);
setStatus("Verified deployment snapshot loaded. Connect a wallet for live StudioNet reads and writes.");
