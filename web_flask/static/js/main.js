function loadHousing() {
  fetch('/api/v1/housing')
      .then(response => response.json())
      .then(data => {
          const listings = data.map(housing => `
              <div>
                  <h3>${housing.name}</h3>
                  <p>${housing.description}</p>
                  <p>City: ${housing.city.name}</p>
                  <p>Price per night: £${housing.price_per_night}</p>
              </div>
          `).join('');
          document.getElementById('housing-listings').innerHTML = listings;
      })
      .catch(error => console.error('Error:', error));
}
