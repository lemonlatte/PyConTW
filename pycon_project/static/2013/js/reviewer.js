var _reviewer_script=function(){
var _num=function(x){return parseFloat($(x).html())}
var recalculate=function(){
    $("tr").each(function(i) {
            var x=$(this).find("td");
            var n=function(t) { return _num(x[t])};
            $(x[7]).html( (n(3)+n(4)*0.1-n(5)*0.1-n(6)).toFixed(1) )
       })
}
recalculate()
$("table").find("a").on("click", function(e){
  e.preventDefault();
  var win=window.open($(this).attr("href"), 'review_window');
  win.focus();
})
var newdiv=$("<div>")
var yourid=$("#drop1").find("b").html()
newdiv.load("http://tw.pycon.org/2013/zh/review/list/"+yourid+"/ table", function(){
var dict={}
newdiv.find("tr").find(".title").find("b").each(function(i) { dict[$(this).html()]=1})
$("tr").each(function(i){var id=$(this).find(".title").find("b").html(); if(id in dict) $(this).css('background', '#99bb99') })
}
)

var newdiv2=$("<div>")
newdiv2.load("http://tw.pycon.org/2013/zh/review/list/ table", function(){
var dict2={}
newdiv2.find("tr").each(function () {
    var id=$(this).find(".title").find("b").html()
        var x=$(this).find("td");
        var n=function(t) { return _num(x[t])};
    dict2[id]=[n(3), n(4), n(5), n(6)]
}
)
$("tr").each(function(i){
    var id=$(this).find(".title").find("b").html()
    if(id in dict2) {
        var xx=dict2[id]
            var x=$(this).find("td");
            var n=function(t) { return _num(x[t])};
        for(var i=0;i<4;i++){
            $(x[i+3]).html(""+xx[i])
        }
    }
})
recalculate()
}
)
}
jQuery.getScript("http://www.datatables.net/download/build/jquery.dataTables.min.js",
    function(){
        $("table").dataTable({"bLengthChange": false, "bPaginate": false})
        $("input[aria-controls]").val("undecided").keyup()
    }
)
_reviewer_script()
$(window).focus(_reviewer_script)
