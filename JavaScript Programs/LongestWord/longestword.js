function longestWord() {
    var sentence = document.querySelector(".string").value;
    var words = sentence.split(" ");
    var longest = 0;
    var lword;

    for (var i = 0; words.length; i++) {
        if (words[i].length > longest) {
            longest = words[i].length;
            lword = words[i];
        }
        // console.log(words[i].length);
    }

    document.querySelector("span").innerText = lword;

}
