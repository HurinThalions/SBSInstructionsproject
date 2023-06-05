function loadAnleitungData() {

    let counter = 0;

    let elements = document.querySelectorAll("li");

    let container = document.getElementById("katalog");

    let anleitungdata = JSON.parse(
        document.getElementById("anleitung-json").textContent);

    // Listelemente werden geladen
    let firstElement = elements[counter];
    let firstIndex = firstElement.dataset.index;
    let firstData = anleitungdata[firstIndex];

    addAnleitung(container, firstData);

    // Alle Elemente werden geladen und angezeigt
    elements.forEach((element) => {
        element.addEventListener("load", function () {
        let index = element.dataset.index;
        let data = anleitungdata[index];
            element.addEventListener("load", function () {
                addAnleitung(container);
            });
        });
    });

function addAnleitung(container, data) {

    let anleitungElement = document.createElement("div");
    anleitungElement.classList.add("anleitung");

    let anleitungtitelElement = document.createElement("p");
    let anleitungtitelText = document.createTextNode(data.anleitungtitel);
    anleitungtitelElement.appendChild(anleitungtitelText);
    anleitungBildElement.classList.add("anleitungtitel");

    let profilElement = document.createElement("p");
    let profilText = document.createTextNode(data.profil);
    profilElement.appendChild(profilText);
    profilElement.classList.add("profil");

    let kategorieElement = document.createElement("p");
    let kategorieText = document.createTextNode(data.kategorie);
    kategorieElement.appendChild(kategorieText);
    kategorieElement.classList.add("kategorie");

    let dauerElement = document.createElement("p");
    let dauerText = document.createTextNode(data.dauer);
    dauerElement.appendChild(dauerText);
    dauerElement.classList.add("dauer");

    let anleitungBildElement = document.createElement("img");
    anleitungBildElement.setAttribute("src", "/media/" + data.anleitungbild);
    anleitungBildElement.classList.add("anleitungbild");
    console.log(data.anleitungbild);

    anleitungElement.appendChild(
        anleitungtitelElement, 
        profilElement, 
        kategorieElement, 
        dauerElement,
        anleitungBildElement);

    container.innerHTML = "";
    container.appendChild(anleitungElement);

    }
}