def get_sum_metrics(predictions, metrics=[]):
    metrics_ = metrics.copy()
    metrics_.append(lambda x: x + 0)
    metrics_.append(lambda x: x + 1)
    metrics_.append(lambda x: x + 2)
    
    #print("metrics[0]:", metrics_[0](predictions))
    #print("metrics[1]:", metrics_[1](predictions))
    #print("metrics[2]:", metrics_[2](predictions))

    #print("Length of metrics:",len(metrics_))

    sum_metrics = 0
    for metric in metrics_:
        #print("eval func: ", metric(predictions))
        sum_metrics += metric(predictions)

    return sum_metrics


def main():
    print(get_sum_metrics(0))  # Should be (0 + 0) + (0 + 1) + (0 + 2) = 3
    print(get_sum_metrics(1))  # Should be (1 + 0) + (1 + 1) + (1 + 2) = 6
    print(get_sum_metrics(2))  # Should be (2 + 0) + (2 + 1) + (2 + 2) = 9
    print(get_sum_metrics(3, [lambda x: x]))  # Should be (3) + (3 + 0) + (3 + 1) + (3 + 2) = 15
    print(get_sum_metrics(0))  # Should be (0 + 0) + (0 + 1) + (0 + 2) = 3
    print(get_sum_metrics(1))  # Should be (1 + 0) + (1 + 1) + (1 + 2) = 6
    print(get_sum_metrics(2))  # Should be (2 + 0) + (2 + 1) + (2 + 2) = 9

if __name__ == "__main__":
    main()
