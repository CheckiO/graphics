from fabric.api import local

def tests():
    """
    Start all tests
    """
    local("python tests/icons_tasks_tests.py")
    local("python tests/icons_interface_tests.py")