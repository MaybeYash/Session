document.getElementById('sessionForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const apiId = document.getElementById('apiId').value;
    const apiHash = document.getElementById('apiHash').value;
    const phoneNumber = document.getElementById('phoneNumber').value;

    if (apiId && apiHash && phoneNumber) {
        const sessionString = `api_id: ${apiId}\napi_hash: ${apiHash}\nphone_number: ${phoneNumber}`;
        document.getElementById('result').textContent = `Generated Session:\n${sessionString}`;
    } else {
        document.getElementById('result').textContent = 'Please fill in all fields.';
    }
});
