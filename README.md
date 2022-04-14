# **Unused Code Identification and Commenting**

We can remove any unused class methods by commenting out them.

## **Prerequisites**

-  Python >= 3.6
-  Vulture (python package)

## **Overview**

To run this script you will need to have Python and Vulture installed on your machine. The instructions to setup Python can be found online. After installing Python, run the following command to install Vulture.

```
pip install vulture
```

## **Implementation**

1. Clone the repository & open the repository root directory in terminal.

2. To comment the unused the code. Run the command with the following pattern.

    ```
    <python> <main.py> <class file path> <usage file path>
    ```

3. We have a class file named `class_file.py`. The usage file is named `usage_file.py`.

4. In `usage_file.py`, we are calling methods from the `class_file.py` which is
    -    displayPublicMembers()

5. In `class_file.py`, the methods which are not being used are
    -   _displayProtectedMembers()
    -   accessPrivateMembers()

6. Open a terminal and run the following command to see the script in action:

    ```
    python main.py class_file.py usage_file.py
    ```

7. The above mentioned unused methods are commented and we can check the code in `class_file.py`.

8. The output we get after running the above mentioned command is

    ```
    <--- Unused Methods --->

    1) _displayProtectedMembers

    2) accessPrivateMembers

    ```
