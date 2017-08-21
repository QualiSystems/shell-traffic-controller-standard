from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.context import ResourceCommandContext

class {{cookiecutter.driver_name}} (ResourceDriverInterface):

    def __init__(self):
        """
        ctor must be without arguments, it is created with reflection at run time
        """
        pass

    def initialize(self, context):
        """
        Initialize the driver session, this function is called everytime a new instance of the driver is created
        This is a good place to load and cache the driver configuration, initiate sessions etc.
        :param InitCommandContext context: the context the command runs on
        """
        pass

    def load_configuration(self, context, config_file_location):
        """
        Load the test configuration file
        :param ResourceCommandContext context: the context object containing resource and reservation info
        :param str config_file_location: The full path in which the configuration file exist. Should include the file name
        """
        pass
        
    def send_arp(self, context):
        """
        Send ARP to populate ARP tables
        :param ResourceCommandContext context: the context object containing resource and reservation info
        """
        pass
        
    def start_emulation(self, context):
        """
        Start device/protocls emulations
        :param ResourceCommandContext context: the context object containing resource and reservation info
        """
        pass
        
    def stop_emulation(self, context):
        """
        Stop device/protocls emulations
        :param ResourceCommandContext context: the context object containing resource and reservation info
        """
        pass
    
    def start_traffic(self, context, blocking):
        """
        Start to run traffic
        :param ResourceCommandContext context: the context object containing resource and reservation info
        :param bool blocking: If set to true, the command will complete ONLY when the test/traffic based on the 
        configuration file is completed and thus no other command can be executed during this time. 
        The default value should be false - in this case the command will complete once the test/traffic is executed
        """
        pass
    
    def stop_traffic(self, context):
        """
        Stop to run traffic
        :param ResourceCommandContext context: the context object containing resource and reservation info
        """
        pass
        
    def get_statistics(self, context, view_name, output_type):
        """
        Get the test/traffic statistics
        :param ResourceCommandContext context: the context object containing resource and reservation info
        :param str view_name: The name of the view for which we want to get its statistics
        :param str output_type: The format of the file in which the statistics will be displayed. The options are: "CSV" or "JSON". Default value is "CSV"
        :return: Returns the statistics based on the requested output type
        :rtype: str
        """
        pass