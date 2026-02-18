document.getElementById('check-btn').addEventListener('click', function() {
    const username = document.getElementById('username').value.trim();
    const resultDiv = document.getElementById('result');

    if (!username) {
        resultDiv.innerHTML = '<p style="color: red;">Please enter a username.</p>';
        return;
    }

    fetch('/detect', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            resultDiv.innerHTML = `<p style="color: red;">${data.error}</p>`;
        } else {
            const color = data.result === 'Fake' ? 'red' : 'green';
            resultDiv.innerHTML = `<p style="color: ${color};">The username is likely ${data.result}.</p>`;
        }
    })
    .catch(error => {
        resultDiv.innerHTML = '<p style="color: red;">An error occurred. Please try again.</p>';
        console.error('Error:', error);
    });
});
