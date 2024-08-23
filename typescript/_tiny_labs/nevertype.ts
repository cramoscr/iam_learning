// Typescript "never" type allows to prevent code
// from execute

function foreverTask(taskName: string) : never {
    while (true) {
        console.log (`Doing ${taskName} over and over again...`);
        break;
    }
}