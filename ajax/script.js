var SpeechRecognition = window.webkitSpeechRecognition;
  
var recognition = new SpeechRecognition();

var Textbox = $('#search');
var instructions = $('instructions');

var Content = '';

recognition.continuous = true;

recognition.onresult = function(event) {

  var current = event.resultIndex;

  var transcript = event.results[current][0].transcript;
 
    Content += transcript;
    Textbox.val(Content);
  
};

recognition.onstart = function() { 
  instructions.text('Voice recognition is ON.');
  console.log('Speech recognition started.');
}

recognition.onspeechend = function() {
  instructions.text('No activity.');
  $("search").click();
  var e = jQuery.Event("keypress");
  e.which = 13; //choose the one you want
  e.keyCode = 13;
  $("#search").trigger(e);
}

recognition.onerror = function(event) {
  if(event.error == 'no-speech') {
    instructions.text('Try again.');
    console.log('Speech recognition error.');
  }
}

$('#start-btn').on('click', function(e) {
  if (Content.length) {
    Content += ' ';
  }
  recognition.start();

  //stoping speach recognition after certain amount of time
  setTimeout(function(){ recognition.stop(); console.log('Speech recognition ended, after 10s.'); }, 10000);
});

Textbox.on('input', function() {
  Content = $(this).val();
})