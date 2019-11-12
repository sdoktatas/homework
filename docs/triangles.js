function classify(a, b, c) {
        if (isNaN(a)) {
            return "Első nem szám";
        }
        a = parseInt(a);

        if (isNaN(b)) {
            return "Második nem szám";
        }
        b = parseInt(b);

        if (isNaN(c)) {
            return "Harmadik nem szám";
        }
        c = parseInt(c);

        if (a <= 0 || b <= 0 || c <= 0) return "Negatív";
        if (a == b && b == c) return "Egyenlő oldalú";
        if (a >= b+c || c >= b+a || b >= a+c) return "Nem háromszög";
        if (b==c || a==b || b==c) return "Egyenlő oldalú";
        return "Általános";
}

window.onload = function() {
    document.getElementById("calculate-button").onclick = function() {
        let a = document.getElementById("a-input").value;
        let b = document.getElementById("b-input").value;
        let c = document.getElementById("c-input").value;

        let result = document.getElementById("result-ul");

        result.innerHTML += "<li>" + "a = " + a + ", b = " + b + ", c = " + c + ": " + classify(a, b, c) + "</li>";
        return false;
    }
};