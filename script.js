document.getElementById("analyzeButton").addEventListener("click", async () => (
const textInput = document.getElementById("textInput").value;
const resultContainer = document.getElementById("resultContainer");
const sentimentResult document.getElementById("sentimentResult");
const emotionResult document.getElementById("emotionResult");

resultContainer.classList.add("hidden");
sentiment Result.textContent = "";
emotionResult.textContent =

if (ItextInput.trim()) (
    alert("Please enter some text to analyze.");
    return;
    
    try {
    const response = await fetch("http://127.0.0.1:5000/analyze"), (
    method: "POST",
    headers: {
        "Content-type": "application/json",
     }, 
     
     body: JSON.stringify({text: textInput)),
    });
    

"Content-Type": "application/json",
    if (!response.ok) (
        throw new Error("Failed to fetch results from the server.");

}
const data await response.json();

// Display the results
sentimentResult.textContent data.sentiment[0].label + (Confidence: " + (data.sentiment[0].score 100).toFixed(2) + "%)";
emotionResult.textContent = data.emotion[0].label +" (Confidence: +(data.emotion[0].score 100).toFixed(2)+")";
resultContainer.classtist.remove("hidden");
} catch (error) (
alert("Error: + error.message);
}
));