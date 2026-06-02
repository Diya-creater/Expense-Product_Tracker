from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

exp=[]
next_id=1

class expenses(BaseModel):
    expense_name:str
    expense_type: str
    expense_description: str
    expense_price: float 
    expense_payment_type: str
#--------------------------------------------Post (add) data in database exp------------------------------------------------
@app.post("/AddExpenses/")
def add_expense(expense: expenses):
    global next_id
    expense_data = expense.dict()
    expense_data["expense_id"] = next_id
    exp.append(expense_data)
    next_id += 1
    return{
        "msg": "Expense added successfully",
        "data": exp
    }

#--------------------------------------------Get (Retrive) data from database------------------------------------------------
@app.get("/getexpense/")
def get_expense():
    return{
        "msg": "Expense added successfully",
        "data": exp
    }

#--------------------------------------------Expense Get_by_Id--------------------------------------------
@app.get("/GetExpenseByID/{expense_id}")
def get_expense_by_id(expense_id: int):

    for expense in exp:
        if expense["expense_id"] == expense_id:
            return {
                "msg": "Expense identified successfully",
                "data": expense
            }

    return {
        "msg": "Expense not found"
    }

#--------------------------------------------Update data in database exp------------------------------------------------
@app.put("/UpdateExpense/{expense_id}")
def update_expense(expense_id: int, update_expense: expenses):
    for expense in exp:
        if expense["expense_id"] == expense_id:
            expense["expense_name"] = update_expense.expense_name
            expense["expense_type"] = update_expense.expense_type
            expense["expense_description"] = update_expense.expense_description
            expense["exopense_price"] = update_expense.expense_price
            expense["expense_payment_type"] = update_expense.expense_payment_type
            return{
                "msg": "Expense data updated successfully",
                "data": expense
            }
            return{
                 "msg": "Expense not found"
            }
        
#--------------------------------------------Data Delete_by_id data in database exp------------------------------------------------        
@app.delete("/deleteExpense/{expense_id}")
def delete_expense(expense_id: int):
    for expense in exp:
        if expense["expense_id"] == expense_id:
            exp.remove(expense)
            return{
            "msg": "Expense data deleted successfully",
            "data": exp
        
        }
    return{
        "msg": "Expense not found"
}

#--------------------------------------------Delete_All_Data data in database exp------------------------------------------------        
@app.delete("/deleteExpense/{expense_id}")
@app.delete("/deleteAllExpense/")
def delete_expense():
            exp.clear()
            return{
            "msg": "Expense data deleted successfully",
            "data": exp
        }