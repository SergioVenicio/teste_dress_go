$(document).ready(function (){
  $("#modal_aluguel").modal();
  $("#login_required").modal();
  $("#calcular").on({
    click: function () {
      var quantidade = $("#quantidade").val();
      var id = $("#id").val();
      $.ajax({
        url: '/api/v1/produtos/' + id,
        success: function (produto) {
          var qntd = parseInt(produto.quantidade);
          if(quantidade > 0 ) {
            if(qntd >= quantidade) {
                var preco = (quantidade * parseFloat(produto.valor)).toFixed(2);
                console.log(preco);
                $("#preco").text(preco);
                $("#modal_alugar").modal();
                $("#alugar").attr('disabled', false);
            } else {
              $("#modal_qntd_erro").modal();
              $("#alugar").attr('disabled', true);
            }
          } else {
            $("#modal_qntd_zero").modal();
            $("#alugar").attr('disabled', true);
          }
        }
      });
    }
  });
});
