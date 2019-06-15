var linkToMP3 = "";

document.querySelector('[role="presentation"]').contentWindow.document.getElementById("recaptcha-anchor").click();

function clickHeadphones() {
    var button = window.document.querySelector('[title="recaptcha challenge"]').contentWindow.document.getElementById("recaptcha-audio-button");
    button.dispatchEvent(new MouseEvent('mouseover'));
    button.dispatchEvent(new MouseEvent('mouseenter'));
    button.click();
    return setTimeout(getLink, 1500);
}

function getLink() {
    linkToMP3 = window.document.querySelector('[title="recaptcha challenge"]').contentWindow.document.getElementsByClassName("rc-audiochallenge-tdownload-link")[0].href;
    console.log(linkToMP3);
    return setTimeout(fetch_and_get_the_job_done, 1000)
}


function fetch_and_get_the_job_done() {
   fetch("http://127.0.0.1:5000/", {"method":"POST", "body":linkToMP3})
  .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    final_answer = myJson["answer"];
    console.log(final_answer);

    document.querySelector('[title="recaptcha challenge"]').contentWindow.document.getElementById('audio-response').value = final_answer;
    window.document.querySelector('[title="recaptcha challenge"]').contentWindow.document.getElementById("recaptcha-verify-button").click();
  });
}

setTimeout(clickHeadphones, 1500)



