'use strict';

document.addEventListener("DOMContentLoaded",function(){
var date = new Date();
var today = new Date(date.getFullYear(), date.getMonth(), date.getDate());

// ** for agent shifts pages start date and end date **
$("#id_start_date").datepicker({
  format: "yyyy-mm-dd",
    viewMode: "days",
    minViewMode: "days",
    autoclose:true,
    clearBtn:true,
    startDate:today
});
$("#id_end_date").datepicker({
  format: "yyyy-mm-dd",
    viewMode: "days",
    minViewMode: "days",
    autoclose:true,
    clearBtn:true,
    startDate:today
});
// ** ** **

// $(function () {
//                $('#id_start_time').datetimepicker({
//                    format: 'LT'
//                });
//            });
    $(function () {
        $("#id_end_time").datetimepicker();
      });
});