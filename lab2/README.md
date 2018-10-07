# Lab 2

This lab is going to explore implementing classification models and comparing them.

# Lab

Use three different classifiers to classify a celestial entity as
a STAR, GALAXY, or QUASAR given only information on the light emitted by
said entity.

Here is the data:

https://drive.google.com/uc?export=download&id=1c3d3YkQtK99iPUEdxE2FaP0GvTXWP5IT


You are going to have to:

1. Grab the data from the internet.
2. Load the data into a Pandas Dataframe.
3. Segment the data into to training and test partitions.
4. Fit 3 models to the data, and use Mean Squared Error to evaluate
which model did the best.
5. Adjust hyperparameters to further optimize each model. (i.e.
adjust neural network layer sizes.)

*NOTE:* A MSE of 0.126 is definitely possible.


# Functional Details

## Reading the data

Pandas comes with a function that reads CSV into a dataframe automatically.
Unfortunately, this accepts a file object, and we don't have the data in a file,
it's on the internet. Rather than saving it to a file and then reading it, we can
put it into a StringIO object, which will behave the same way as a file object.

```Python
data = pd.read_csv(
    io.StringIO(
        requests.get(
            "https://drive.google.com/uc?export=download&id=1c3d3YkQtK99iPUEdxE2FaP0GvTXWP5IT"
        ).text
    )
)
```

Splitting the data is just a matter of using slice syntax at a desired index. To
find our split index, let's take 80% of the data for training. Let's also assume
that the dependent variable is the last column.

```Python
split_index = int(len(data) * 0.8)
target_col = len(data.columns) - 1
```

Now make some numpy arrays and slice on that index:

```Python
all_X = np.array([x[1:target_col] for x in data.values])
all_Y = np.array([ classification_map[x[target_col]]  for x in data.values])

train_X = all_X[ : split_index],
train_Y = all_Y[ : split_index],
test_X = all_X[split_index : ],
text_Y = all_Y[split_index : ]
```

## Object Orientation

You may have noticed that Python is largely object oriented. Many libraries
leverage objects (Classes) to expose functionality to users. An object is
an entity in code that has properties and functionality. A `Pandas` `Dataframe`
is a good example of this.  One of its pieces of functionality is to read in
a CSV file, and its properties include the data it read in and their column
details.

As it happens, `sklearn` is also largely object oriented. Here is an
example:

```Python
clf = RandomForestClassifier(max_depth=15, random_state=0)
clf.fit(train_X, train_Y)
pred_Y = clf.predict(test_X)
print("Random Forest:")
print("\tMean squared error:", mean_squared_error(test_Y, pred_Y))
```

Notice how a `Random Forest Classifier` is created. Then it retains its
state to the next line where it is fit to data.  It continues to retain
its state to later predict against test data.

You can see all of the `Random Forest Classifier`'s properties and
functions [here](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html).

Find more information on Object Oriented Programming [here](https://python.swaroopch.com/oop.html).




