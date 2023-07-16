(function () {
  // Create an empty array to store marker locations
  var locations = [];

  // Create a map with Leaflet
  var map = L.map('map');

  // Create a tile layer and add it to the map
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors',
    maxZoom: 18,
  }).addTo(map);

  // Retrieve user locations from the server and add them to the locations array
  fetch('/users/user-locations/')
    .then(response => response.json())
    .then(data => {
      data.forEach(user => {
        if (user.latitude !== null && user.longitude !== null) {
          locations.push([user.latitude, user.longitude]);

          // Create a marker for the user location
          var marker = L.marker([user.latitude, user.longitude]);

          // Create a custom popup content with Bootstrap classes
          var popupContent = `
            <div class="popup-content">
              <h3><a href="/users/user-details/${user.id}/" style="text-decoration: none;">${user.username}</a></h3>
              <p class="mb-1">Email: ${user.email}</p>
              <p class="mb-1">Latitude: ${user.latitude}</p>
              <p class="mb-1">Longitude: ${user.longitude}</p>
              <p class="mb-0">Home Address: ${user.home_address}</p>
            </div>
          `;

          marker.bindPopup(popupContent);

          // Add the marker to the map only if the latitude and longitude are valid
          marker.addTo(map);
        }
      });

      // Fit the map view to the bounds of the user locations
      map.fitBounds(locations);
    });
})();
