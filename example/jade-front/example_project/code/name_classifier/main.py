from name_classifier.train import Trainer

def main():
    trainer = Trainer()
    trainer.load()
    trainer.train()


if __name__ == '__main__':
    main()
