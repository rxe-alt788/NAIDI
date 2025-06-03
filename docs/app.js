function sha256(str) {
  const encoder = new TextEncoder();
  return crypto.subtle.digest("SHA-256", encoder.encode(str)).then(buf => {
    return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, "0")).join("");
  });
}

async function checkHash() {
  const text = document.getElementById("article").value;
  const hash = await sha256(text);
  fetch("../registry/registry.json")
    .then(r => r.json())
    .then(data => {
      const match = data.find(item => item.hash === hash);
      const resultDiv = document.getElementById("result");
      if (match) {
        resultDiv.innerHTML = `<p>✅ Match found!</p><pre>${JSON.stringify(match, null, 2)}</pre>`;
      } else {
        resultDiv.innerHTML = "❌ No match found.";
      }
    });
}

