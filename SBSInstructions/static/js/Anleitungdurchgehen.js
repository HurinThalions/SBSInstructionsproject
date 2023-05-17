// function loadAnleitungData() {
    
//     fetch('schritt_dict.json')
//         .then(response => response.json)
//         .then(data => console.log(data));
// }

function loadAnleitungData1() {

    let elements = document.querySelectorAll('li');
    let container = document.getElementById('schritt-details');

    // Holt die daten aus dem html und speichert sie in jsondata
    let jsondata = JSON.parse(document.getElementById('schritte-json').textContent);
    console.log(jsondata);
    

    // Entfernt informationen aus dem Container wenn neue gelden werden
    let container1 = document.getElementById('einzelschritte');


    elements.forEach(element => {
        element.addEventListener('click', function() {
            removeContainerChildren(container)
            addEinzelschritt(container, element)
        })
    })

    function addEinzelschritt(container, schrittElement) {

        let index = schrittElement.dataset.index
        let data = jsondata[index]
        console.log(data)

        let schrittbenennungElement = document.createElement('h1')
        let benunngText = document.createTextNode(data.schrittbenennung)
        schrittbenennungElement.appendChild(benunngText)

        let schrittbeschreibungElement = document.createElement('p')
        let beschreibungText = document.createTextNode(data.schrittbeschreibung)
        schrittbeschreibungElement.appendChild(beschreibungText)

        container.append(schrittbenennungElement, schrittbeschreibungElement)
    }

    function removeContainerChildren(container) {
        while (container.firstChild) {
            container.removeChild(container.firstChild)
        }
    }

}
