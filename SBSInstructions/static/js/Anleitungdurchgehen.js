function loadAnleitungData1() {
    let elements = document.querySelectorAll('li');
    let container = document.getElementById('schritt-details');
    let jsondata = JSON.parse(document.getElementById('schritte-json').textContent);
    let kompdata = JSON.parse(document.getElementById('komponenten-json').textContent);
  
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
      let anleitungsschrittId = data.id; // ID des aktuellen Anleitungsschritts
      let komponentenContainer = document.createElement('div');
//    komponentenContainer.innerHTML = ''; // Leeren Sie den Container, bevor Sie die Komponenten hinzufügen
  
      let komponenten = kompdata.filter(komponente => komponente.anleitungsschritt_id === anleitungsschrittId);
  
      komponenten.forEach(komponente => {
        let komponenteElement = document.createElement('div');
        komponenteElement.classList.add('komponente');
        komponenteElement.textContent = komponente.kompbeschreibung;
        komponentenContainer.appendChild(komponenteElement);
        container.appendChild(komponentenContainer)
      });
      
    }
  
    function removeContainerChildren(container) {
      while (container.firstChild) {
        container.removeChild(container.firstChild);
      }
    }
  }
  
  loadAnleitungData1();



// function loadAnleitungData1() {
//     let elements = document.querySelectorAll('li');
//     let container = document.getElementById('schritt-details');
//     let jsondata = JSON.parse(document.getElementById('schritte-json').textContent);
//     let kompdata = JSON.parse(document.getElementById('komponenten-json').textContent);
//     console.log(jsondata);
//     console.log(kompdata);

//     let firstElement = elements[0];
//     let firstIndex = firstElement.dataset.index;
//     let firstData = jsondata[firstIndex];

//     addEinzelschritt(container, firstData);
//     addKomponenten(container, firstData);

//     elements.forEach((element) => {
//         element.addEventListener('click', function() {
//             removeContainerChildren(container);
//             let index_schritte = element.dataset.index;
//             let data = jsondata[index_schritte];
//             let index_komponenten = element.dataset.index;
//             let dataKomponenten = kompdata[index_komponenten];
//             addEinzelschritt(container, data);
//             addKomponenten(container, dataKomponenten);
//         });
//     });

//     function addEinzelschritt(container, data) {
//         let einzelschrittElement = document.createElement('div');
//         einzelschrittElement.classList.add('einzelschritt');

//         let schrittbenennungElement = document.createElement('h1');
//         let benennungText = document.createTextNode(data.schrittbenennung);
//         schrittbenennungElement.appendChild(benennungText);

//         let beschreibungElement = document.createElement('p');
//         let beschreibungText = document.createTextNode(data.beschreibung);
//         beschreibungElement.appendChild(beschreibungText);

//         einzelschrittElement.appendChild(schrittbenennungElement);
//         einzelschrittElement.appendChild(beschreibungElement);

//         container.innerHTML = '';
//         container.appendChild(einzelschrittElement);
//     }

//     function addKomponenten(container, dataKomponenten) {
//         let komponentenElement = document.createElement('div');
//         komponentenElement.classList.add('komponenten');
            
//         // ersteSchrittKomponenten.forEach((komponente) => {
//         let komponenteElement = document.createElement('div');
//         komponenteElement.classList.add('komponente');

//         let komponentenBeschreibungElement = document.createElement('h3')
//         let beschreibungText = document.createTextNode(dataKomponenten.kompbeschreibung)
//         komponentenBeschreibungElement.appendChild(beschreibungText)
//         komponentenElement.appendChild(komponenteElement);
//         // });

//         container.appendChild(komponentenElement);
//       }

//     function removeContainerChildren(container) {
//         while (container.firstChild) {
//             container.removeChild(container.firstChild);
//         }
//     }
// }

// loadAnleitungData1();
