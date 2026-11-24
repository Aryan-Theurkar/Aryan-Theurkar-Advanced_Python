import logging

logging.basicConfig(
    filename="program.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

try:
    logging.info("Program Started")

    a = 10
    b = 0

    logging.debug("Performing division")

    c = a / b

    print(c)

except Exception as e:
    logging.error("Error occurred: %s", e)

finally:
    logging.info("Program Finished")

print("Check program.log file")
