async function get_news() {
    let response = await fetch("http://localhost:8000");
    if (response.ok) {
        let json = await respone.json();
        return json;
    } else {
        alert("Исправь ошибку с HTTP:" + response.status)
    }
}