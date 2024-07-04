#include </usr/local/mysql-connector-c++-8.0.31/include/jdbc/mysql_driver.h>
#include </usr/local/mysql-connector-c++-8.0.31/include/jdbc/mysql_connection.h>

#include </usr/local/mysql-connector-c++-8.0.31/include/jdbc/cppconn/driver.h>
#include </usr/local/mysql-connector-c++-8.0.31/include/jdbc/cppconn/exception.h>
#include </usr/local/mysql-connector-c++-8.0.31/include/jdbc/cppconn/resultset.h>

#include </usr/local/mysql-connector-c++-8.0.31/include/jdbc/cppconn/statement.h>

#include <iostream>



int main() {
    try {
        // Create a driver instance
        sql::mysql::MySQL_Driver* driver = sql::mysql::get_mysql_driver_instance();

        // Create a connection
        std::unique_ptr<sql::Connection> con(driver->connect("tcp://127.0.0.1:3306", "root", "P@ssw0rd"));

        // Connect to the MySQL database
        con->setSchema("F1");

        // Create a statement object
        std::unique_ptr<sql::Statement> stmt(con->createStatement());

        // Execute a query
        std::unique_ptr<sql::ResultSet> res(stmt->executeQuery("SELECT Race FROM 2023_season_race_data"));

        // Iterate through the result set and print results
        while (res->next()) {
            std::cout << "Race = " << res->getInt("id") << ", ";
            // std::cout << "name = " << res->getString("name") << std::endl;
        }
    } catch (sql::SQLException& e) {
        std::cerr << "SQLException: " << e.what() << std::endl;
        std::cerr << "MySQL error code: " << e.getErrorCode() << std::endl;
        std::cerr << "SQLState: " << e.getSQLState() << std::endl;
    }

    return 0;
}
