function loadAnleitungData1() {
    let elements = document.querySelectorAll('li');
    let container = document.getElementById('schritt-details');
    let jsondata = JSON.parse(document.getElementById('schritte-json').textContent);

    let firstElement = elements[0];
    let firstIndex = firstElement.dataset.index;
    let firstData = jsondata[firstIndex];

    addEinzelschritt(container, firstData);
    addKomponenten(container, firstData);

    elements.forEach((element) => {
        element.addEventListener('click', function() {
            removeContainerChildren(container);
            let index = element.dataset.index;
            let data = jsondata[index];
            addEinzelschritt(container, data);
            addKomponenten(container, data);
        });
    });

    function addEinzelschritt(container, data) {
        let einzelschrittElement = document.createElement('div');
        einzelschrittElement.classList.add('einzelschritt');

        let schrittbenennungElement = document.createElement('h1');
        let benennungText = document.createTextNode(data.schrittbenennung);
        schrittbenennungElement.appendChild(benennungText);

        let beschreibungElement = document.createElement('p');
        let beschreibungText = document.createTextNode(data.beschreibung);
        beschreibungElement.appendChild(beschreibungText);

        einzelschrittElement.appendChild(schrittbenennungElement);
        einzelschrittElement.appendChild(beschreibungElement);

        container.innerHTML = '';
        container.appendChild(einzelschrittElement);
    }

    function addKomponenten(container, data) {
        let komponentenElement = document.createElement('div');
        komponentenElement.classList.add('komponenten');

        data.komponenten.forEach((komponente) => {
            let komponenteElement = document.createElement('div');
            komponenteElement.classList.add('komponente');
            komponenteElement.textContent = komponente;
            komponentenElement.appendChild(komponenteElement);
        });

        container.appendChild(komponentenElement);
    }

    function removeContainerChildren(container) {
        while (container.firstChild) {
            container.removeChild(container.firstChild);
        }
    }
}

loadAnleitungData1();