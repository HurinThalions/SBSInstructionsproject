// function loadAnleitungData() {
    
//     fetch('schritt_dict.json')
//         .then(response => response.json)
//         .then(data => console.log(data));
// }

function loadAnleitungData1() {

    var schritt_dict = JSON.parse(document.getElementById('schritt_dict'));
    console.log(schritt_dict);

}