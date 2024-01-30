class ProfitabilityCalculator:
    def __init__(self, units_sold, foc_proposal_percentage, fms_percentage, foc_agent, rebate_proposal_percentage,
                 agent_commission, logistic_costs, cif_price, wsp_price, ifrs_percentage, rpm_cost_per_unit, oh_cost_per_unit):
        self.units_sold = units_sold
        self.foc_proposal_percentage = foc_proposal_percentage
        self.fms_percentage = fms_percentage
        self.foc_agent = foc_agent
        self.rebate_proposal_percentage = rebate_proposal_percentage
        self.agent_commission = agent_commission
        self.logistic_costs = logistic_costs
        self.cif_price = cif_price
        self.wsp_price = wsp_price
        self.ifrs_percentage = ifrs_percentage
        self.rpm_cost_per_unit = rpm_cost_per_unit
        self.oh_cost_per_unit = oh_cost_per_unit

    def calculate_profitability(self):
        # Calculate relevant metrics
        package_price_to_public = self.cif_price * (1 + self.fms_percentage)
        package_price_to_pharmacy = package_price_to_public * (1 - self.rebate_proposal_percentage)
        gross_sales = package_price_to_pharmacy * self.units_sold
        rebate_proposal = gross_sales * self.rebate_proposal_percentage
        ifrs = gross_sales - rebate_proposal
        net_sales = ifrs - (self.rpm_cost_per_unit + self.oh_cost_per_unit)
        cogs_amount = (self.rpm_cost_per_unit + self.oh_cost_per_unit) * self.units_sold
        gp = net_sales - cogs_amount
        gp_after_agent_and_logistic = gp - (self.agent_commission + self.logistic_costs)
        gp_percentage = (gp_after_agent_and_logistic / gross_sales) * 100

        # Print the results
        print(f"\nProfitability Calculation Results:")
        print(f"----------------------------------")
        print(f"Gross Sales: {gross_sales:.2f}")
        print(f"Rebate Proposal: {rebate_proposal:.2f}")
        print(f"IFRS: {ifrs:.2f}")
        print(f"Net Sales: {net_sales:.2f}")
        print(f"COGS Amount: {cogs_amount:.2f}")
        print(f"Gross Profit: {gp:.2f}")
        print(f"GP After Agent and Logistic: {gp_after_agent_and_logistic:.2f}")
        print(f"Gross Profit Percentage: {gp_percentage:.2f}%")

# Input parameters
units_sold = float(input("Enter the units expected to be sold: "))
foc_proposal_percentage = float(input("Enter the FOC Proposal percentage: "))
fms_percentage = float(input("Enter the FMS percentage: "))
foc_agent = float(input("Enter the FOC Agent: "))
rebate_proposal_percentage = float(input("Enter the Rebate Proposal percentage: "))
agent_commission = float(input("Enter the Agent Commission: "))
logistic_costs = float(input("Enter the Logistic/Post & Courier/Destruction costs: "))
cif_price = float(input("Enter the CIF Price: "))
wsp_price = float(input("Enter the WSP Price: "))
ifrs_percentage = float(input("Enter the IFRS percentage: "))
rpm_cost_per_unit = float(input("Enter the RPM Cost per unit: "))
oh_cost_per_unit = float(input("Enter the OH Cost per unit: "))

# Create an instance of ProfitabilityCalculator
calculator = ProfitabilityCalculator(units_sold, foc_proposal_percentage, fms_percentage, foc_agent,
                                     rebate_proposal_percentage, agent_commission, logistic_costs,
                                     cif_price, wsp_price, ifrs_percentage, rpm_cost_per_unit, oh_cost_per_unit)

# Calculate and display profitability
calculator.calculate_profitability()
