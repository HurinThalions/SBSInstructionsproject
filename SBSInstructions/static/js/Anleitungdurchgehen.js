function loadAnleitungData1() {

    let counter = 0;
    let elements = document.querySelectorAll('li');
    let container = document.getElementById('schritt-details');

    // Laden der Daten aus dem context von views.py
    let jsondata = JSON.parse(document.getElementById('schritte-json').textContent);
    let kompdata = JSON.parse(document.getElementById('komponenten-json').textContent);

    let firstElement = elements[counter];
    let firstIndex = firstElement.dataset.index;
    let firstData = jsondata[firstIndex];
  
    addEinzelschritt(container, firstData);
    addKomponenten(container, firstData);
  
    elements.forEach((element) => {
      element.addEventListener('load', function() {
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
      komponentenContainer.innerHTML = ''; // Leeren Sie den Container, bevor Sie die Komponenten hinzufügen
  
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

    function nextAnleitungsschritt() {
        counter++;
        if (counter >= elements.length) {
          counter = 0;
        }
        let nextElement = elements[counter];
        let nextIndex = nextElement.dataset.index;
        let nextData = jsondata[nextIndex];
        removeContainerChildren(container);
        addEinzelschritt(container, nextData);
        addKomponenten(container, nextData);
      }
    
      let buttonElement = document.getElementById('buttonkleinrechts');
      buttonElement.addEventListener('click', nextAnleitungsschritt);
  }
  
  loadAnleitungData1();
