$(function() {
  $('.cpf').mask('000.000.000-00', {reverse: true});
  $('.date').mask('00/00/0000');
  $('.criadoData').mask('00/00/0000 00:00:00');
  $('.TelCelular').mask('(00) 00000-0000');
  $('.TelFixo').mask('(00) 0000-0000');
  $('.cep').mask('00000-000');
});
$( function() {
$( “#datepicker” ).datepicker();
} );