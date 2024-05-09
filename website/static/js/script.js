function submitForm(event) {
    event.preventDefault(); // Prevent default form submission

    var formData = new FormData(event.target); // Get form data

    // Send an AJAX request to the Flask route to fetch weather data
    fetch('/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json()) // Parse response as JSON
    .then(data => {
        // Update card elements with the new weather data
        // For example, assuming 'cardContainer' is the ID of the container for the cards
        var cardContainer = document.getElementById("cardContainer");
        cardContainer.innerHTML = ""; // Clear existing cards
        data.forEach(weatherInfo => {
            // Create card element and populate with weatherInfo data
            var card = document.createElement("div");
            card.classList.add("card");
            // Populate card with weatherInfo data (e.g., weatherInfo.city_name, weatherInfo.temp, etc.)
            // Append card to cardContainer
            cardContainer.appendChild(card);
        });
    })
    .catch(error => console.error('Error:', error));
}
