document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('file-input');
    const uploadBtn = document.getElementById('upload-btn');
    const imagePreviewContainer = document.getElementById('image-preview-container');
    const imagePreview = document.getElementById('image-preview');
    const resultContainer = document.getElementById('result-container');
    const predictionText = document.getElementById('prediction-text');
    const confidenceText = document.getElementById('confidence-text');
    const spinner = document.getElementById('spinner');

    // Trigger file input when the button is clicked
    uploadBtn.addEventListener('click', () => {
        fileInput.click();
    });

    // Handle file selection
    fileInput.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
            // Show image preview
            const reader = new FileReader();
            reader.onload = (e) => {
                imagePreview.src = e.target.result;
                imagePreviewContainer.classList.remove('hidden');
            };
            reader.readAsDataURL(file);

            // Hide previous results and show spinner
            resultContainer.classList.add('hidden');
            spinner.classList.remove('hidden');

            // Send file to the backend for prediction
            predict(file);
        }
    });

    // Function to send the image for prediction
    async function predict(file) {
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();
            
            if (!response.ok) {
                // This handles errors sent from the Flask app (like "Please upload a tomato leaf")
                throw new Error(data.error || 'An unknown error occurred.');
            }
            
            // Display a successful prediction
            displaySuccess(data);

        } catch (error) {
            // Display an error message
            displayError(error.message);
        } finally {
            // Hide spinner
            spinner.classList.add('hidden');
        }
    }

    function displaySuccess(data) {
        resultContainer.classList.remove('error');
        predictionText.classList.remove('error-text');
        
        predictionText.textContent = data.predicted_class;
        confidenceText.textContent = `Confidence: ${data.confidence}`;
        resultContainer.classList.remove('hidden');
    }

    function displayError(errorMessage) {
        resultContainer.classList.add('error');
        predictionText.classList.add('error-text');

        predictionText.textContent = errorMessage;
        confidenceText.textContent = ''; // Clear confidence on error
        resultContainer.classList.remove('hidden');
    }
});
