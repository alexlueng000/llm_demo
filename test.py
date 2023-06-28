from utils import CodeReviewerPromptTemplate

reviewer = CodeReviewerPromptTemplate(input_variables=["source_code"], template="")

source_code = """

func listStuff(wg *sync.WaitGroup, workerID int, inputChan chan int, outputChan chan int) {
	defer wg.Done()

	for i := range inputChan {
		//fmt.Println("sending ", i)
		outputChan <- i
	}
}

func List(workers int) ([]int, error) {
	_output := make([]int, 0)

	inputChan := make(chan int, 1000)
	outputChan := make(chan int, 1000)

	var wg sync.WaitGroup
	wg.Add(workers)

	fmt.Printf("+++ Spinning up %v workers\n", workers)
	for i := 0; i < workers; i++ {
		go listStuff(&wg, i, inputChan, outputChan)
	}

	for i := 0; i < 3000; i++ {
		inputChan <- i
	}

	done := make(chan struct{})
	go func() {
		close(done)
		close(inputChan)
		close(outputChan)
		wg.Wait()
	}()

	for o := range outputChan {
		fmt.Println("reading from channel...")
		_output = append(_output, o)
	}

	<-done
	fmt.Printf("+++ output len: %v\n", len(_output))
	return _output, nil
}
"""

prompt = reviewer.format(source_code=source_code)

print(prompt)