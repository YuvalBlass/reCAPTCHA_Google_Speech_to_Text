document.querySelector('[role="presentation"]').contentWindow.document.getElementById("recaptcha-anchor").click();

var button = window.document.querySelector('[title="recaptcha challenge"]').contentWindow.document.getElementById("recaptcha-audio-button");
button.dispatchEvent(new MouseEvent('mouseover'));
button.dispatchEvent(new MouseEvent('mouseenter'));
button.click();

linkToMP3 = window.document.querySelector('[title="recaptcha challenge"]').contentWindow.document.getElementsByClassName("rc-audiochallenge-tdownload-link")[0].href;

fetch("http://127.0.0.1:5000/", {"mode":'no-cors', "method":"POST", "body":linkToMP3})
  .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    final_answer = myJson["answer"]
    console.log(final_answer)

    document.querySelector('[title="recaptcha challenge"]').contentWindow.document.getElementById('audio-response').value = final_answer;
    window.document.querySelector('[title="recaptcha challenge"]').contentWindow.document.getElementById("recaptcha-verify-button").click();
  });



