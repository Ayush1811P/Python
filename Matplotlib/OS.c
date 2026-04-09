#include <stdio.h>

int main()
{
    int total_memory, block_size, num_blocks, external_fragmentation;
    
    int num_processes;
    int process_memory[10];
    
    int allocated_blocks = 0;
    int total_internal_fragmentation = 0;
    int process_index, block_index;
    
    printf("========== MEMORY CONFIGURATION ==========\n");
    printf("Enter total memory available (in Bytes): ");
    scanf("%d", &total_memory);
    
    printf("Enter block size (in Bytes): ");
    scanf("%d", &block_size);
    
    num_blocks = total_memory / block_size;
    external_fragmentation = total_memory % block_size;
    
    printf("\n========== PROCESS INPUT ==========\n");
    printf("Enter number of processes: ");
    scanf("%d", &num_processes);
    
    for(process_index = 0; process_index < num_processes; process_index++)
    {
        printf("Process %d - Memory required (Bytes): ", process_index + 1);
        scanf("%d", &process_memory[process_index]);
    }
    
    printf("\n========== MEMORY ALLOCATION RESULTS ==========\n");
    printf("Total blocks available: %d\n", num_blocks);
    printf("\n%-10s %-20s %-15s %-20s\n", "PROCESS", "MEMORY REQUIRED", "ALLOCATED", "INTERNAL WASTE");
    printf("%-10s %-20s %-15s %-20s\n", "-------", "----------------", "---------", "---------------");
    
    for(process_index = 0; process_index < num_processes && allocated_blocks < num_blocks; process_index++)
    {
        int current_process = process_index + 1;
        int required_memory = process_memory[process_index];
        int internal_waste;
        
        printf("%-10d %-20d ", current_process, required_memory);
        
        if(required_memory > block_size)
        {
            printf("%-15s %-20s\n", "NO", "---");
        }
        else
        {
            internal_waste = block_size - required_memory;
            printf("%-15s %-20d\n", "YES", internal_waste);
            
            total_internal_fragmentation += internal_waste;
            allocated_blocks++;
        }
    }
    
    printf("\n========== FRAGMENTATION SUMMARY ==========\n");
    
    if(process_index < num_processes)
    {
        printf("⚠ WARNING: Memory is FULL!\n");
        printf("Processes %d to %d could not be accommodated.\n", 
               process_index + 1, num_processes);
    }
    
    printf("\nTotal Internal Fragmentation: %d bytes (wasted within blocks)\n", 
           total_internal_fragmentation);
    printf("Total External Fragmentation: %d bytes (unused memory remainder)\n", 
           external_fragmentation);
    
    return 0;
}
