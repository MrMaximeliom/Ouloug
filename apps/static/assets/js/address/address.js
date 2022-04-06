'use strict';

document.addEventListener("DOMContentLoaded",function(){
let data_list = JSON.parse($('#my-data').html())
console.log(data_list)
 $("#filter_by").change(function(){
        var selectedValue = $(this).children("option:selected").val();
        var filter_value = $("#filter_value");

//  *** start handling search form for state page ***

        if (selectedValue == "country" || selectedValue == "currency")
        {
        console.log(selectedValue)
        filter_value.empty();
        $.each(data_list["countries_list"], function(key,value) {
        console.log(value["name"])
        filter_value.append($("<option></option>")
        .attr("value", value["name"]).text(value["name"]));

        });

        }
// their is also filter status for city pages
        else if(selectedValue == "status"){
        filter_value.empty();
         $.each(data_list["status"], function(key,value) {
        console.log(value[1])
         filter_value.append($("<option></option>")
        .attr("value", value[0]).text(value[1]));

        });
        }
//  *** end handling search form for state page ***

//  *** start handling search form for city page ***

        else if (selectedValue == "state")
        {
        filter_value.empty();
        $.each(data_list["states_list"], function(key,value) {
        console.log(value["name"])
        filter_value.append($("<option></option>")
        .attr("value", value["name"]).text(value["name"]));

        });

        }

//  *** end handling search form for state page ***
//  *** start handling search form for agent shifts page ***

        else if (selectedValue == "team")
        {
        filter_value.empty();
        $.each(data_list["teams_list"], function(key,value) {
        console.log(value["name"])
        filter_value.append($("<option></option>")
        .attr("value", value["name"]).text(value["name"]));

        });

        }

//  *** end handling search form for state page ***
//  *** start handling search form for telecom numbers page ***

        else if (selectedValue == "telecom")
        {
        filter_value.empty();
        $.each(data_list["telecoms_list"], function(key,value) {
        console.log(value["name"])
        filter_value.append($("<option></option>")
        .attr("value", value["name"]).text(value["name"]));

        });

        }
     else if(selectedValue == "type"){
        filter_value.empty();
         $.each(data_list["type"], function(key,value) {
        console.log(value[1])
         filter_value.append($("<option></option>")
        .attr("value", value[0]).text(value[1]));

        });
        }

//  *** end handling search form for telecom numbers page ***
//  *** start handling search form for customers page ***
        else if (selectedValue == "city")
        {
        filter_value.empty();
        $.each(data_list["cities_list"], function(key,value) {
        console.log(value["name"])
        filter_value.append($("<option></option>")
        .attr("value", value["name"]).text(value["name"]));

        });

        }
                else if (selectedValue == "business_type")
        {
        filter_value.empty();
        $.each(data_list["business_types_list"], function(key,value) {
        filter_value.append($("<option></option>")
        .attr("value", value["type_name"]).text(value["type_name"]));

        });

        }
             else if(selectedValue == "account_status"){
        filter_value.empty();
         $.each(data_list["account_status"], function(key,value) {
        console.log(value[1])
         filter_value.append($("<option></option>")
        .attr("value", value[0]).text(value[1]));

        });
        }
        else if(selectedValue == "purchase_status"){
        filter_value.empty();
         $.each(data_list["purchase_status"], function(key,value) {
        console.log(value[1])
         filter_value.append($("<option></option>")
        .attr("value", value[0]).text(value[1]));

        });
        }
//  *** end handling search form for customers page ***


    });

});