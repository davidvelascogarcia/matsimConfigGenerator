'''
  * ***************************************************************
  *      Program: MATSim Config Generator
  *      Type: Python
  *      Author: David Velasco Garcia @davidvelascogarcia
  * ***************************************************************
'''

# Libraries
import os
os.environ["OPENCV_IO_MAX_IMAGE_PIXELS"] = pow(2,40).__str__()

import argparse
import datetime
from halo import Halo
import platform


class MATSimConfigGenerator:

    # Function: Constructor
    def __init__(self):

        # Build Halo spinner
        self.systemResponse = Halo(spinner='dots')

        # Build parser element
        parser = argparse.ArgumentParser()
        parser.add_argument("--network", "-n", default="network.xml", help="Input xml network.")
        parser.add_argument("--plans", "-p", default="plans.xml", help="Input xml plans.")
        parser.add_argument("--output", "-o", default="./output", help="Output simulation dirs.")

        # Parse arguments
        args = parser.parse_args()
        self.network = args.network
        self.plans = args.plans
        self.output = args.output

    # Function: getSystemPlatform
    def getSystemPlatform(self):

        # Get system configuration
        print("\nDetecting system and release version ...\n")
        systemPlatform = platform.system()
        systemRelease = platform.release()

        print("**************************************************************************")
        print("Configuration detected:")
        print("**************************************************************************")
        print("\nPlatform:")
        print(systemPlatform)
        print("Release:")
        print(systemRelease)

        return systemPlatform, systemRelease

    # Function: generateConfigFile
    def generateConfigFile(self):

        try:
            path = "./config.xml"
            file = open(str(path), 'w+')
            file.write('<?xml version="1.0" ?>\n')
            file.write('<!DOCTYPE config SYSTEM "http://www.matsim.org/files/dtd/config_v2.dtd">\n')
            file.write('<config>\n')

            file.write('<module name="network">\n')
            file.write('<param name="inputNetworkFile" value="' + str(self.network) + '" />\n')
            file.write('</module>\n')

            file.write('<module name="plans">\n')
            file.write('<param name="inputPlansFile" value="' + str(self.plans) + '" />\n')
            file.write('</module>\n')

            file.write('<module name="controler">\n')
            file.write('<param name="outputDirectory" value="' + str(self.output) + '" />\n')
            file.write('<param name="firstIteration" value="0" />\n')
            file.write('<param name="lastIteration" value="10" />\n')
            file.write('</module>\n')

            file.write('<module name="planCalcScore">\n')
            file.write('<parameterset type="activityParams">\n')
            file.write('<param name="activityType" value="h" />\n')
            file.write('<param name="typicalDuration" value="12:00:00" />\n')
            file.write('</parameterset>\n')
            file.write('<parameterset type="activityParams">\n')
            file.write('<param name="activityType" value="w" />\n')
            file.write('<param name="typicalDuration" value="8:00:00" />\n')
            file.write('</parameterset>\n')
            file.write('</module>\n')

            file.write('<module name="strategy">\n')
            file.write('<param name="maxAgentPlanMemorySize" value="5" />\n')
            file.write('<parameterset type="strategysettings">\n')
            file.write('<param name="strategyName" value="BestScore"/>\n')
            file.write('<param name="weight" value="0.9"/>\n')
            file.write('</parameterset>\n')
            file.write('<parameterset type="strategysettings">\n')
            file.write('<param name="strategyName" value="ReRoute"/>\n')
            file.write('<param name="weight" value="0.1"/>\n')
            file.write('</parameterset>\n')
            file.write('</module>\n')
            file.write('</config>\n')
            file.close()

            systemResponseMessage = "\n[INFO] Config file generated correctly.\n"
            self.systemResponse.text_color = "green"
            self.systemResponse.succeed(systemResponseMessage)

        except Exception as ex:
            systemResponseMessage = "\n[ERROR] Error, generating config file.\n"
            self.systemResponse.text_color = "red"
            self.systemResponse.fail(systemResponseMessage)

    # Function: processRequests
    def processRequests(self):

        print("\n**************************************************************************")
        print("Processing request:")
        print("**************************************************************************\n")

        try:
            # Get initial time
            initialTime = datetime.datetime.now()

            # Generate config file
            self.generateConfigFile()

            systemResponseMessage = "\n[INFO] Request done correctly.\n"
            self.systemResponse.text_color = "green"
            self.systemResponse.succeed(systemResponseMessage)

            # Get end time
            endTime = datetime.datetime.now()

            # Compute elapsed time
            elapsedTime = endTime - initialTime

            systemResponseMessage = "\n[INFO] Elapsed time: " + str(elapsedTime) + ".\n"
            self.systemResponse.text_color = "blue"
            self.systemResponse.info(systemResponseMessage)

        except:
            systemResponseMessage = "\n[ERROR] Error, processing request.\n"
            self.systemResponse.text_color = "red"
            self.systemResponse.fail(systemResponseMessage)


# Function: main
def main():

    print("**************************************************************************")
    print("**************************************************************************")
    print("                   Program: MATSim Config Generator                       ")
    print("                     Author: David Velasco Garcia                         ")
    print("                             @davidvelascogarcia                          ")
    print("**************************************************************************")
    print("**************************************************************************")

    print("\nLoading MATSim Config Generator engine ...\n")

    # Build matsimConfigGenerator object
    matsimConfigGenerator = MATSimConfigGenerator()

    # Get system platform
    systemPlatform, systemRelease = matsimConfigGenerator.getSystemPlatform()

    # Process input requests
    matsimConfigGenerator.processRequests()

    print("**************************************************************************")
    print("Program finished")
    print("**************************************************************************")
    print("\nmatsimConfigGenerator program finished correctly.\n")

    userExit = input()


if __name__ == "__main__":

    # Call main function
    main()