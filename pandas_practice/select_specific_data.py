def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(students)
    return students[students['student_id']==101][['name', 'age']]
