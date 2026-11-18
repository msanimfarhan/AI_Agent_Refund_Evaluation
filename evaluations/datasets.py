from deepeval.dataset import EvaluationDataset, Golden 
from deepeval.test_case import ToolCall 


dataset = EvaluationDataset(
    goldens = [
        Golden(
            input="I am user123, i would like a refund for the book and the pen",
            expected_output="A refund ticket for 30$ has been issued successfully",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
                ToolCall(name="calculate_right_refund"),
                ToolCall(name="issue_refund_ticket"),
                ToolCall(name="get_today_date")
            ]
        ),
        Golden(
                    input="I am user123, i would like a refund for the book",
                    expected_output="A refund ticket for 23$ has been issued successfully",
                    expected_tools=[
                        ToolCall(name="get_user_purchase_history"),
                        ToolCall(name="calculate_right_refund"),
                        ToolCall(name="issue_refund_ticket"),
                        ToolCall(name="get_today_date")
                    ]
                ),
        Golden(
                            input="I am user123, i would like no refund, i just want to know what to purchase",
                            expected_output="no refund ticket is issued only a list of items purchased",
                            expected_tools=[
                                ToolCall(name="get_user_purchase_history")
                            ]
                        ),  
        Golden(
                                    input="I am user999, i would like no refund, i just want to know what to purchase",
                                    expected_output="tell the user that the username is not valid and ask for username again before giving any info about refund",
                                    expected_tools=[
                                        ToolCall(name="get_user_purchase_history")
                                    ]
                                ), 
        Golden(
                            input="I am user126, i would like a refund for water_bottle",
                            expected_output="no redund given because it is oustside of the 30 days guideline",
                            expected_tools=[
                                ToolCall(name="get_user_purchase_history"),
                                ToolCall(name="get_today_date")
                            ]
                        ),
        Golden(
                            input="I am user126, i would like a refund for backpack and water_bottle",
                            expected_output="A refund ticket of 45$ has been issued successfully but only for the backpack but the water_bottle is not eligible for the refund because it is outside 30 days refund policy",
                            expected_tools=[
                                ToolCall(name="get_user_purchase_history"),
                                ToolCall(name="calculate_right_refund"),
                                ToolCall(name="issue_refund_ticket"),
                                ToolCall(name="get_today_date")
                            ]
                        ),
        Golden(
                            input="I am user126, i would like a refund for sneakers",
                            expected_output="no refund is given as you have not purchased the item",
                            expected_tools=[
                                ToolCall(name="get_user_purchase_history")
                            ]
                        ),
    ]
)