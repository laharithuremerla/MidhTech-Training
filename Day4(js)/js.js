function addStudent() {

    let input = document.getElementById("studentName");
    let name = input.value.trim();

    if (name === "") {
        alert("Please enter a student name!");
        return;
    }

    let li = document.createElement("li");

    let span = document.createElement("span");
    span.innerText = name;

    let btn = document.createElement("button");
    btn.innerText = "Delete";
    btn.className = "deleteBtn";

    btn.onclick = function () {
        li.remove();
    };

    li.appendChild(span);
    li.appendChild(btn);

    document.getElementById("studentList").appendChild(li);

    // input.value = "";
}uu