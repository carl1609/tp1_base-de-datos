document.addEventListener("DOMContentLoaded", () => {

    const keywords = ["FROM", "WHERE", "ORDER BY"];
    const textElement = document.getElementById("consulta");
    let textContent = textElement.innerHTML;

    keywords.forEach(keyword => {
        const regex = new RegExp(`(${keyword})`, "gi");
        textContent = textContent.replace(regex, `<br>$1`);
    });

    textElement.innerHTML = textContent;
});