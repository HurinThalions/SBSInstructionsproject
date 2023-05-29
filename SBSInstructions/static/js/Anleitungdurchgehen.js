function loadAnleitungData1() {
  let counter = 0;

  // Alle Listelemente aus views.py werden geholt
  let elements = document.querySelectorAll("li");

  // container in dem die daten geladen werden wird geholt
  let container = document.getElementById("schritt-details");

  // Laden der Daten aus dem context von views.py in lesbarem Format
  let jsondata = JSON.parse(
    document.getElementById("schritte-json").textContent
  );
  let kompdata = JSON.parse(
    document.getElementById("komponenten-json").textContent
  );

  // Listenelement wird geladen
  let firstElement = elements[counter];
  let firstIndex = firstElement.dataset.index;
  let firstData = jsondata[firstIndex];

  // anzeigen des elements
  addEinzelschritt(container, firstData);
  addKomponenten(container, firstData);

  // Alle Elemente werden geladen und angezeigt
  // Diesen teil verstehe ich noch nicht ganz. Doppelung mit dem Codeteil darüber?
  elements.forEach((element) => {
      let index = element.dataset.index;
      let data = jsondata[index];
    element.addEventListener("load", function () {
      removeContainerChildren(container);
      addEinzelschritt(container, data);
      addKomponenten(container, data);
    });
  });

  // Einzelner Schritt wird geholt und auf die Seite geladen
  // Schrittbild fehlt noch
  function addEinzelschritt(container, data) {
    let einzelschrittElement = document.createElement("div");
    einzelschrittElement.classList.add("einzelschritt");

    let schrittbenennungElement = document.createElement("h1");
    let benennungText = document.createTextNode(data.schrittbenennung);
    schrittbenennungElement.appendChild(benennungText);

    let beschreibungElement = document.createElement("p");
    let beschreibungText = document.createTextNode(data.beschreibung);
    beschreibungElement.appendChild(beschreibungText);

    let schrittBildElement = document.createElement("img");
    schrittBildElement.setAttribute("src", "/media/" + data.schrittbild);
    console.log(data.schrittbild);

    einzelschrittElement.appendChild(schrittbenennungElement);
    einzelschrittElement.appendChild(beschreibungElement);
    einzelschrittElement.appendChild(schrittBildElement);

    container.innerHTML = "";
    container.appendChild(einzelschrittElement);
  }

  // Komponenten die zum derzeitugem Schritt gehoeren werden geholt und auf der die Seite geladen
  function addKomponenten(container, data) {
    // ID des aktuellen Anleitungsschritts
    let anleitungsschrittId = data.id;
    let komponentenContainer = document.createElement("div");

    // Leeren des Containers bevor neue Komponenten hinzugefuegt werden
    komponentenContainer.innerHTML = "";

    // Komponenten werden anhand des ForeignKeys gefiltert
    let komponenten = kompdata.filter(
      (komponente) => komponente.anleitungsschritt_id === anleitungsschrittId
    );

    // Komponenten werden auf die Seite geladen
    // Komponentenbild fehlt noch
    komponenten.forEach((komponente) => {
      let komponenteElement = document.createElement("div");
      komponenteElement.classList.add("komponente");
      komponenteElement.textContent = komponente.kompbeschreibung;
      komponentenContainer.appendChild(komponenteElement);
      container.appendChild(komponentenContainer);
    });
  }

  // Entfernen des Anleitungsschritts und der Komponenten
  function removeContainerChildren(container) {
    while (container.firstChild) {
      container.removeChild(container.firstChild);
    }
  }

  // Laden der naechsten Anleitungsschritts
  function nextAnleitungsschritt() {
    counter++;

    // Wenn letzter Schritt erreicht wird, wird eine neue Seite geladen
    if (counter >= elements.length) {
      window.location.pathname = "SBSInstructionsproject/anleitungfertig";
      return;
    }

    // naechtses Element wird geholt
    let nextElement = elements[counter];
    let nextIndex = nextElement.dataset.index;
    let nextData = jsondata[nextIndex];

    // naechtes Element wird geladen
    removeContainerChildren(container);
    addEinzelschritt(container, nextData);
    addKomponenten(container, nextData);
  }

  // Button der geklickt wird, um zu dem naechsten Anleitungsschritt zu kommen
  let buttonElementnaechster = document.getElementById("buttonkleinrechts");
  buttonElementnaechster.addEventListener("click", nextAnleitungsschritt);

  function previousAnleitungsschritt() {
    counter--;
    if (counter < 0) {
          
          // Popup für Anleitung Abbrechen? -> Ja/Nein
          // wenn ja -> window.location.pathname = "SBSInstructionsproject/Startbildschirm";
          // wenn nein -> counter = 0;
    }
    let previousElement = elements[counter];
    let previousIndex = previousElement.dataset.index;
    let previousData = jsondata[previousIndex];
    removeContainerChildren(container);
    addEinzelschritt(container, previousData);
    addKomponenten(container, previousData);
  }

  // Button der geklickt wird, um zu dem vorherigem Anleitungsschritt zu kommen
  let buttonElementzurueck = document.getElementById("buttonkleinlinks");
  buttonElementzurueck.addEventListener("click", previousAnleitungsschritt);
}

loadAnleitungData1();
