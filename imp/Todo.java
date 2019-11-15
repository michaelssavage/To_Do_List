import java.io.File;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.util.Scanner;
import java.io.FileNotFoundException;


public class Todo {
    
    public static void main(String[] args) {

        boolean jobNotEntered = true;

        System.out.println("Available commands.\n" +
            "'add e' to add an event.\n" +
            "'add t' to add a task.\n" +
            "'r to remove most recent job.\n" +
            "'job' to print the most recent job\n" +
            "'all' to print the all jobs\n" +
            "'q' to quit.");

        while(jobNotEntered){

            System.out.println("Enter command: ");
            
            Scanner in = new Scanner(System.in);
            String job = in.nextLine();

            if(job.equals("add e")){

                addEvent();
            }   
            if(job.equals("add t")){

                addTask();
            }

            if(job.equals("r")){

                remove();
            }

            if(job.equals("job")){

                showJob();
            }

            if(job.equals("all")){

                printAll();
            }

            if(job.equals("q")){

                jobNotEntered = false;
            }
        }
    }

    public static void addTask() {

        try(FileWriter f = new FileWriter("toDoList.txt", true);
            BufferedWriter bw = new BufferedWriter(f);
            PrintWriter file = new PrintWriter(bw)){

            System.out.println("Tasks have a date, a start time," + 
            "a duration and a list of people assigned to the task.");

            Scanner in = new Scanner(System.in);
            System.out.println("Enter task name: ");
            String name = in.nextLine();
            System.out.println("Enter date: ");
            String date = in.nextLine();
            System.out.println("Enter start time: ");
            String time = in.nextLine();
            System.out.println("Enter duration: ");
            String duration = in.nextLine();
            System.out.println("Enter list of people assigned to the task: ");
            String people = in.nextLine();

            file.println(name + ": " + date + ", " +
            time + ", "  + duration + ", "  + "[" + people + "]");

        } 
        catch (IOException e) {
            System.out.println("Unable to write to file.");
        }
    }

    public static void addEvent() {

        try(FileWriter f = new FileWriter("toDoList.txt", true);
            BufferedWriter bw = new BufferedWriter(f);
            PrintWriter file = new PrintWriter(bw)){

            System.out.println("An event has a date, " +
            "a start time and a location. ");

            Scanner in = new Scanner(System.in);
            System.out.println("Enter event name: ");
            String name = in.nextLine();
            System.out.println("Enter date: ");
            String date = in.nextLine();
            System.out.println("Enter start time: ");
            String time = in.nextLine();
            System.out.println("Enter location: ");
            String location = in.nextLine();

            file.println(name + ": "  + date + ", " +
            time + ", "  + location);

        } 
        catch (IOException e) {
            System.out.println("Unable to write to file.");
        }
    }

    public static void remove(){

        try{
            File inputFile = new File("toDoList.txt");

            File tempFile = new File(inputFile.getAbsolutePath() + ".tmp");
            BufferedReader br = new BufferedReader(new FileReader(inputFile));
            PrintWriter pw = new PrintWriter(new FileWriter(tempFile));
            String line = null;

            String remove = br.readLine();
            while ((line = br.readLine()) != null) {
                pw.println(line);
                pw.flush();
            }
            pw.close();
            br.close();

            //Delete the original file
            if (!inputFile.delete()) {
                System.out.println("Could not delete file");
                return;
            }

            //Rename the new file to the filename the original file had.
            if (!tempFile.renameTo(inputFile))
                System.out.println("Could not rename file");
            }
        catch(IOException e){
            System.out.println("File not found.");
        }
    }

    public static void showJob(){
        try{
            File todo = new File("toDoList.txt");
            Scanner in = new Scanner(todo);

            boolean notEmpty = todo.length() != 0;
            if(notEmpty){
                String job = in.nextLine();
                System.out.println(job);
            }
        }
        catch(FileNotFoundException e){
            System.out.println("File not found.");
        }
    }

    public static void printAll(){

        try{
            File todo = new File("toDoList.txt");
            Scanner in = new Scanner(todo);

            boolean notEmpty = todo.length() != 0;
            if(notEmpty){

                while(in.hasNextLine()){

                    String job = in.nextLine();
                    System.out.println(job);
                }
            }
        }
        catch(FileNotFoundException e){
            System.out.println("File not found.");
        }
    }
}
