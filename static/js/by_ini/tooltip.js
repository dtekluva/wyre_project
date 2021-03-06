

tippy('#baseline-card', {
    content: `<strong>
                Baseline Energy is derived using multiple linear regression.<hr/>
                Shows the total energy expected to be used based on history as current expected temperature
                <br>

                <ul>
                    <li>
                        Atleast 6 months of data is required for highest accuracy.
                    </li>
                </ul>

            </strong>`,
        placement: "right-start"
    });

tippy('#felf-card', {
        content: `
                    <strong>
                        PEAK TO AVG POWER RATIO.<hr/>
                        <ul>
                            
                            <li>
                                Describes the disparity between peak and average power demand of a facility. 
                            </li>
                            <li>
                                The higher the ratio the better, the lower the ratio the worse. 
                            </li>
                        </ul>

                    </strong>
                `,
        placement: "right-start"
    });

tippy('#capacity-card', {
    content: `
                <strong>
                    Generator Size Efficiency<hr/>

                    <ul>
                        
                        <li>
                            Describes energy usage efficiency of facility generators. <br>
                        </li>
                        <br>
                        <li>
                            70% of total rated capacity is the more standardized value higher values signify overloading
                        </li>
                    </ul>

                </strong>
            `,
    placement: "right-start"
    });
tippy('#fuel-card', {
    content: `
                <strong>
                    Generator Fuel and hours of usage.
                    <br>

                </strong>
            `,
    placement: "right-start"
    });
tippy('#emissions-card', {
    content: `
                <strong>
                    Facility carbon foot print for all energy sources<hr/>
                    <ul>

                        Metrics                        
                        <li>
                            For grid supply - 0.562kgCO2 per kWh 
                            <br>
                         </li>
                         <li>
                            For diesel - 2.68kgCO2 per liter
                            <br>
                        </li>
                        <br>
                        <li>
                        Note that the Units are metric kilograms and Metric Tons (M-Tons)
                        </li>
                        <br>
                        <li>
                        A tree can absorb as much as 48 pounds of carbon dioxide per year and can sequester 1 ton of carbon dioxide by the time it reaches 40 years old.
                        </li>



                    </ul>

                </strong>
            `,
    placement: "right-start"
    });