$(document).ready(function() {
    //Built in search function
    $( "#search-btn" ).click(function() {					
        Job = $('#intro-keywords').val()
        Location = $('#autocomplete-input').val()
        search_url = '/search/'+Job+'/'+Location+'/1'
        window.open(search_url,"_self")
    });

    $( "#FilterSearch" ).click(function() {		
        
        salary = $('#SalaryRange').attr('value')
        salaryRange = salary.split(",");

        $( ".job-listing" ).each(function() {
            salary = []
            salary[0] = parseFloat($(this).find('div.job-listing-details').attr('data-minimum'))
            salary[1] = parseFloat($(this).find('div.job-listing-details').attr('data-maximum'))
            salaryRange[0] = parseFloat(salaryRange[0]);
            salaryRange[1] = parseFloat(salaryRange[1]);

            console.log(salary[0],salaryRange[0],salaryRange[1])
            if(salaryRange[0] <= salary[0] && salary[0] <= salaryRange[1]){
                if(salaryRange[0] <= salary[0] && salary[0] <= salaryRange[1]){
                    $(this).show();  
                }
            }else{
                $(this).hide();
            }



            // if(salary != 'Competitive salary'){


            //     if(salaryRange[0] >= salary[0] >= salaryRange[1]){
            //         $(this).hide();
            //     }

            // }else{
            //     $(this).hide();
            // }
        });

    });
});




