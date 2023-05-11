// function loadAnleitungData() {
    
//     fetch('schritt_dict.json')
//         .then(response => response.json)
//         .then(data => console.log(data));
// }

function loadAnleitungData1() {

    var schrittDataElement = document.getElementById('schrittData');
    var schritt = JSON.parse(schrittDataElement.textContent);
    console.log(schritt);

}