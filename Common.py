import pytest
class common:
    def validate_dynamic_table(self,expected_dynamic_table_value,actual_dynamic_table_value):
        print("validate_dynamic_table method is started")
        try:
            if expected_dynamic_table_value==actual_dynamic_table_value:
                print("dynamic table data is correct")
            else:
                pytest.fail("dynamic table data is not correct. Expetected value is {expected} and actual value is {actual}".format(expected=expected_dynamic_table_value,actual=actual_dynamic_table_value))
        except Exception as e:
            pytest.fail("validate_dynamic_table method is failed")
            print(e)
