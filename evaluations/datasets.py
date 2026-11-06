from deepeval.dataset import EvaluationDataset, Golden 
from deepeval.test_case import ToolCall 

dataset = EvaluationDataset(
    golden = [
        Golden(
            input="I am user123, i would like a refund for the book and the pen",
            expected_output="A refund ticket for 30$ has been issued successfully",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
                ToolCall(name="alculate_right_refund"),
                ToolCall(name="issue_refund_ticket"),
                ToolCall(name="get_today_date")
            ]
        ),
        Golden(
                    input="I am user123, i would like a refund for the book",
                    expected_output="A refund ticket for 23$ has been issued successfully",
                    expected_tools=[
                        ToolCall(name="get_user_purchase_history"),
                        ToolCall(name="alculate_right_refund"),
                        ToolCall(name="issue_refund_ticket"),
                        ToolCall(name="get_today_date")
                    ]
                ),

        Golden(
                            input="I am user123, i would like no refund, i just want to know what to purchase",
                            expected_output="A refund ticket for 23$ has been issued successfully",
                            expected_tools=[
                                ToolCall(name="get_user_purchase_history"),
                                ToolCall(name="alculate_right_refund"),
                                ToolCall(name="issue_refund_ticket"),
                                ToolCall(name="get_today_date")
                            ]
                        )


    ]
)