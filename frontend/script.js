function updateStatus() {
    fetch("http://127.0.0.1:5000/status")
        .then(response => response.json())
        .then(data => {
            document.getElementById("word").innerText = "Kelime: " + data.word;
            document.getElementById("lives").innerText = "Can: " + data.lives;
        });
}

function guessLetter() {
    const letter = document.getElementById("letter").value;

    fetch("http://127.0.0.1:5000/guess", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ letter: letter })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("word").innerText = "Kelime: " + data.word;
        document.getElementById("lives").innerText = "Can: " + data.lives;
    });

    document.getElementById("letter").value = "";
}

window.onload = updateStatus;

