import matplotlib.pyplot as plt
import numpy as np

def plotTheClusters(output):
    plt.figure(figsize=(16,6))

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', 
    'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan', 
    'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 
    'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 
    'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 
    'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 
    'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 
    'honeydew', 'hotpink', 
    'indianred', 'indigo', 'ivory', 
    'khaki', 
    'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 
    'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 
    'navajowhite', 'navy', 
    'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 
    'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 
    'red', 'rosybrown', 'royalblue', 
    'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 
    'tan', 'teal', 'thistle', 'tomato', 'turquoise', 
    'violet', 
    'wheat', 'white']

    plt.subplot(121)

    for i, cluster in enumerate(output):
        plt.scatter([i]*len(cluster), cluster, color=colors[i])
    plt.xlabel('Cluster')
    plt.ylabel('Values')
    plt.title('Clusters Plot')


    plt.subplot(122)
    flat_data = np.array([val for sublist in output for val in sublist])
    plt.plot(np.arange(len(flat_data)), flat_data, 'o')
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.title('Flat Data Plot')
    
    fig = plt.gcf()
    plt.close()

    return fig

